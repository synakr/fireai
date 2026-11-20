import React from "react";
import { createRoot } from "react-dom/client";
import { UploadPage } from "./components/UploadPage";
import "./ui/guest.css";

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <UploadPage />
  </React.StrictMode>,
);
