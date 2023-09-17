import React, { useEffect, useState } from "react";
import { Textarea, Button, ButtonGroup, Center, Spinner, Grid, Text, VStack, Modal, ModalOverlay, ModalContent, ModalHeader, ModalFooter, ModalBody, ModalCloseButton, useDisclosure } from '@chakra-ui/react';

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
  const [comment, setComment] = useState('');
  const [modalInfo, setModalInfo] = useState('');
  const [comments, setComments] = useState([]);

  const getAppletInfo = (appletName) => {
    // Fetch or compute the information for the applet.
    // For now, let's just return a sample message.
    return `This is a sample ${appletName} applet available for download. \n You can save it to your applets.`;
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
          <Center key={i} w="150px" h="100px" bg="#fad7f5" borderRadius="10px">
            <VStack>
              <Text>{app}</Text>
              <Button onClick={() => handleClick(app)}>Info</Button>
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

            {/* Display Comments */}
            {comments.map((com, idx) => (
                <Text key={idx} mt={3}>
                    <Text style={{ color: 'gray' }}>Comment from User38573: {com}</Text>
                </Text>
            ))}
            {/* Adding comment section below */}
            <Textarea
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                placeholder="Add your comment here..."
                mt={4} // adds margin top for spacing
            />

            {/* Adding comment section below */}

          </ModalBody>
          <ModalFooter>
            <ButtonGroup spacing={4}>
            <Button onClick={() => {
                // Append the new comment to the list of comments
                setComments(prevComments => [...prevComments, comment]);
                // Clear the current comment for the next input
                setComment('');
                // Close the modal
                // onClose();
            }}>Submit Comment</Button>
                <Button variant="outline" mr={3} onClick={onClose}>
                Close
                </Button>
                <Button colorScheme="blue">Save</Button>
            </ButtonGroup>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Center>
  );
}

export default MyApplets;
