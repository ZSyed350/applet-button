const express = require('express');
const bodyParser = require('body-parser');
const Docker = require('dockerode');
const fs = require('fs');
const streamBuffers = require('stream-buffers');
const app = express();
const docker = new Docker();
containersMap = {}
app.use(bodyParser.json());


app.post('/start', async (req, res) => {
    const { scriptName } = req.body;
    const folderPath = `./${scriptName}`
    const scriptNameWithExtension = scriptName + ".py"
    const scriptPath = `${folderPath}/${scriptNameWithExtension}`;
    console.log(scriptPath);
    if (!fs.existsSync(scriptPath)) {
        return res.status(404).send('Script not found.');
    }

    try {
        // Create a temporary Dockerfile
        try {
            await fs.mkdir(`${folderPath}`);
            console.log('Directory created successfully!');
        } catch (error) {
            console.error('Error creating directory:', error);
        }
        const dockerfilePath = `${folderPath}/Dockerfile`;
        fs.writeFileSync(dockerfilePath, `
            FROM python:3.9
            WORKDIR /app
            COPY ${scriptNameWithExtension} .
            CMD ["python", "${scriptNameWithExtension}"]
            RUN mkfifo /tmp/my_pipe
        `);
            
        // Build the image
        const imageName = `python-repl-${scriptName}`;
        await docker.buildImage({
            context: folderPath,
            src: ["./Dockerfile", scriptNameWithExtension]
        }, {t: imageName});

        // Cleanup temporary Dockerfile
        fs.unlinkSync(dockerfilePath);

        // Start a container using the image
        const container = await docker.createContainer({
            Image: imageName,
            AttachStdin: true,
            AttachStdout: true,
            Tty: true,
            OpenStdin: true,
            StdinOnce: false
        });

        await container.start();
        containersMap[container.id] = container
        res.json({ status: 'script started', containerId: container.id });
    } catch (err) {
        res.status(500).send(err.message);
    }
});


app.post('/input', async (req, res) => {
    try {
        const { userInput, containerId } = req.body;
        const container = containersMap[containerId];

        if (container) {
            // Write the userInput to the named pipe
            const cmd = `echo "${userInput}" > /tmp/my_pipe`;
            const exec = await container.exec({
                AttachStdout: true,
                AttachStderr: true,
                Cmd: ["/bin/sh", "-c", cmd]
            });

            const stream = await exec.start();
            const outputBuffer = new streamBuffers.WritableStreamBuffer();
            container.modem.demuxStream(stream, outputBuffer, outputBuffer);

            stream.on('end', () => {
                const output = outputBuffer.getContentsAsString();
                res.json({ result: output });
            });
        } else {
            res.status(400).send("Script not started");
        }
    } catch (err) {
        res.status(500).send(err.message);
    }
});




app.listen(3001, () => {
    console.log('REPL server listening on port 3001');
});
