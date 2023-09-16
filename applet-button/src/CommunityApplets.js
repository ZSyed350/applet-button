import React, { useEffect, useState } from "react";
import { Button, Center, Spinner, Grid, Text, VStack, Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton, useDisclosure } from '@chakra-ui/react';

async function getApps() {
  const response = await fetch("http://localhost:8080/get_community_apps", {
    method: "POST",
  });
  if (response.ok) {
    const json = await response.json();
    return json;
  }
}

function MyApplets() {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [applets, setApps] = useState([]);
  const [modalInfo, setModalInfo] = useState('');

  const getAppletInfo = (appletName) => {
    // Fetch or compute the information for the applet.
    // For now, let's just return a sample message.
    return `This is a sample ${appletName} applet available for download`;
  };

  const handleClick = (app) => {
    setModalInfo(getAppletInfo(app));
    onOpen();
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
        <Spinner /> {/* Note: You need to import Spinner from Chakra UI for this line to work */}
      </Center>
    );

  return (
    <Center p="1em">
      <Grid templateColumns="repeat(3, 1fr)" gap={3}>
        {applets.map((app, i) => (
          <Center key={i} w="150px" h="100px" bg="#fca2f0" borderRadius="10px">
            <VStack>
              <Text>{app}</Text>
              <Button onClick={() => handleClick(app)}>Download</Button>
            </VStack>
          </Center>
        ))}
      </Grid>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Applet Information</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            {modalInfo}
          </ModalBody>
          <ModalFooter>
            <Button variant="ghost" onClick={onClose}>Close</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Center>
  );
}

export default MyApplets;
