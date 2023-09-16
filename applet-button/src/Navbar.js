// Navbar.js
import { HStack, Center } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <HStack className="navbar" bgColor="#323232">
      <Center w="100%">
        <Link to="/">Home</Link>
        <Link to="/generate">Generate Applet</Link>
        <Link to="/my-apps">My Applets</Link>
        {/* <Link to="shared-apps">Community</Link> */}
        <Link to="about">About</Link>
      </Center>
    </HStack>
  );
}

export default Navbar;
