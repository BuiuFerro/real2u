import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        <label>Insira a URL da imagem:</label>
        <form method="POST" action=".">
          <p><input id="input-box" type="text" name="url" /></p>
          <p><input id="button" type="submit" value="Gerar contornos!" /></p>
        </form>
        <a
          className="App-link"
          href="https://github.com/BuiuFerro/real2u"
          target="_blank"
          rel="noopener noreferrer"
        >
          Source code of this app
        </a>
      </header>
    </div>
  );
}

export default App;
