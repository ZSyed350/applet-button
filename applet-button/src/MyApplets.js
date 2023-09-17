// Terminal.js
import { Button, Text, Center, Spinner, VStack } from "@chakra-ui/react";
import React, { useEffect, useState } from "react";
// import Grid from "./Grid";
import { Grid } from "@chakra-ui/react";

async function getApps() {
  const response = await fetch("http://localhost:8080/get_my_apps", {
    method: "POST",
  });
  if (response.ok) {
    const json = await response.json();
    return json;
  }
}

async function runApplet(data) {
  const response = await fetch("http://localhost:8080/run-applet", {
    method: "POST",
    body: data,
  });
  if (response.ok) {
    const json = await response.json();
    return json;
  }
}

function MyApplets() {
  const [applets, setApps] = useState([]);
  const [responseFromServer, setResponseFromServer] = useState("");

  const handleClick = async (app_name) => {
    const data = { app_name };

    // Make POST request to Flask server
    fetch("/run-applet", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        setResponseFromServer(data.result); // assuming server sends back JSON response with "result" field
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    alert(`Request to run: ${app_name}`);
  };

  async function loadApps() {
    const response = await getApps();
    setApps(response.applets);
  }

  useEffect(() => {
    loadApps();
  }, []);

  if (applets.length === 0)
    return (
      <Center>
        <Spinner />
      </Center>
    );

  return (
    <Center p="1em">
      <Grid templateColumns="repeat(3, 1fr)" gap={3}>
        {applets.map((app, i) => (
          <Center key={i} w="100px" h="100px" bg="#7eb7ed" borderRadius="10px">
            <VStack>
              <Text>{app}</Text>
              <Button onClick={() => handleClick(app)}>Run</Button>
            </VStack>
          </Center>
        ))}
      </Grid>

      <Grid></Grid>
      {/* <Text>adsfiuosafhioasdhfiahf</Text> */}
      {/* <Button>Test</Button> */}
    </Center>
  );
}

export default MyApplets;
