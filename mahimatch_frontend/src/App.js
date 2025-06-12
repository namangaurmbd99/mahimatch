import { BrowserRouter, Routes, Route } from "react-router-dom";
import Signin from "./Components/Signin/Signin";
import Signup from "./Components/Signup/Signup";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/signin" element={<Signin />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
