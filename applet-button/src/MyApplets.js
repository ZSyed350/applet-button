// Terminal.js
import { Box, Button, Text } from "@chakra-ui/react";
import React, { useEffect } from "react";
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

function MyApplets() {
  const [apps, setApps] = React.useState([]);

  useEffect(() => {
    const response = getApps();
    response.then((data) => {
      console.log(data);
      setApps(data);
    });
  }, []);

  return (
    <Box>
      <Grid>
        {apps.length > 0 &&
          apps.map((app) => <Box key={app.id}>{app.name}</Box>)}
      </Grid>
      <Text>adsfiuosafhioasdhfiahf</Text>
      <Button>Test</Button>
    </Box>
  );
}

export default MyApplets;
