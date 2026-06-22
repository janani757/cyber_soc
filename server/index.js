const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json({ limit: "50mb" }));

app.get("/", (req, res) => {
  res.send("Cyber Threat Detection Backend Running");
});

// Single Prediction
app.post("/analyze", async (req, res) => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/predict",
      req.body
    );

    res.json(response.data);

  } catch (error) {

    res.status(500).json({
      error: error.message
    });

  }
});

// CSV Batch Analysis
app.post("/analyze-csv", async (req, res) => {
  try {

    const response = await axios.post(
      "http://127.0.0.1:8000/analyze_csv",
      req.body
    );

    res.json(response.data);

  } catch (error) {

    res.status(500).json({
      error: error.message
    });

  }
});

app.listen(5000, () => {
  console.log("Backend running on port 5000");
});