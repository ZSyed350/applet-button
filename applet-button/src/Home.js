import { Center, HStack } from "@chakra-ui/react";
import { Heading, VStack, Button, Text } from "@chakra-ui/react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <Center height="90vh">
      <VStack spacing="3em">
        <Heading>DAN</Heading>

        <Text>A simpler way of creating and sharing your own AI-generated applets.</Text>

        <HStack>
          <Link to="/generate">
            <Button>Get Started</Button>
          </Link>
          <Link to="/about">
            <Button>Learn More</Button>
          </Link>
        </HStack>
      </VStack>
    </Center>
  );
};

export default Home;
