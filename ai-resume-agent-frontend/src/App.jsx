import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Applications from "./pages/Applications";
import Analytics from "./pages/Analytics";
import Recommendations from "./pages/Recommendations";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/applications"
          element={<Applications />}
        />

        <Route
          path="/analytics"
          element={<Analytics />}
        />

        <Route
          path="/recommendations"
          element={<Recommendations />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;