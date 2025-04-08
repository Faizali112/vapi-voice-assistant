const express = require('express');
const cors = require('cors');
const axios = require('axios');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 3000;

app.post('/webhook', async (req, res) => {
    const event = req.body;

    console.log('Received event:', event);

    if (event.type === 'call_started') {
        return res.send({ text: "Hello! How can I help you today?" });
    }

    if (event.type === 'user_said') {
        const userMessage = event.payload.transcript;

        try {
            const completion = await axios.post(
                'https://api.openai.com/v1/chat/completions',
                {
                    model: "gpt-4o",
                    messages: [
                        { role: "system", content: "You are a helpful voice assistant for customer support." },
                        { role: "user", content: userMessage }
                    ]
                },
                {
                    headers: {
                        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`
                    }
                }
            );

            const botResponse = completion.data.choices[0].message.content;
            return res.send({ text: botResponse });

        } catch (error) {
            console.error("OpenAI Error:", error.response?.data || error.message);
            return res.send({ text: "Sorry, something went wrong." });
        }
    }

    res.sendStatus(200);
});

app.listen(PORT, () => {
    console.log(`✅ Server is running on http://localhost:${PORT}`);
});
