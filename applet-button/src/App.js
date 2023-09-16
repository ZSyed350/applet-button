import { ChakraProvider } from "@chakra-ui/react";
import React from "react";
import { BrowserRouter, Route, Router, Routes } from "react-router-dom";
import "./App.css"; // Import the styles
import MyApplets from "./MyApplets";
import NavBar from "./Navbar";
import Terminal from "./Terminal";
import Home from "./Home";

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
          </Routes>
        </ChakraProvider>
      </BrowserRouter>
    </>
  );
}

export default App;
