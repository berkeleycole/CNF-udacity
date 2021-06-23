'use strict';

const express = require('express');
const app = express();

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// Routes
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
