import { ChakraProvider } from "@chakra-ui/react";
import React from "react";
import { BrowserRouter, Route, Router, Routes } from "react-router-dom";
import "./App.css"; // Import the styles
import MyApplets from "./MyApplets";
import NavBar from "./Navbar";
import Terminal from "./Terminal";
import Home from "./Home";
import CommunityApplets from "./CommunityApplets";
import AppTerminal from "./AppTerminal";

function App() {
  return (
    <>
      <BrowserRouter>
        <ChakraProvider>
          <NavBar />

          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/generate" element={<Terminal />}></Route>
            <Route path="/my-apps" element={<MyApplets />}></Route>
            <Route path="/shared-apps" element={<CommunityApplets />}></Route>
            <Route path="/run-app" element={<AppTerminal />}></Route>
          </Routes>
        </ChakraProvider>
      </BrowserRouter>
    </>
  );
}

export default App;
