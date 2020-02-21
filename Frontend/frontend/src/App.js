import React from 'react';

import Taskbar from "./components/Taskbar/Taskbar";

function App() {
  return (
    <div>
      <header>
        <Taskbar/>
      </header>
      <div>
        Body
      </div>
      <footer>
        Footer
      </footer>
    </div>
  );
}

export default App;
