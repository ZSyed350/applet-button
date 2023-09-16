// Navbar.js
import { HStack } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <HStack className="navbar">
      <Link to="/">Home</Link>
      <Link to="/generate">Generate Applet</Link>
      <Link to="/my-apps">My Applets</Link>
      {/* <Link to="shared-apps">Community</Link> */}
      {/* <Link to="about">About</Link> */}
    </HStack>
  );
}

export default Navbar;
