import Anthropic from "@anthropic-ai/sdk";
import { betaTool } from "@anthropic-ai/sdk/helpers/beta/json-schema";

const client = new Anthropic();

// The same two lookups we ran by hand — wrapped as tools via betaTool()
// so toolRunner() knows their name, description and input schema.
const getWeather = betaTool({
  name: "get_weather",
  description: "Get the current weather for a city.",
  inputSchema: {
    type: "object",
    properties: {
      city: { type: "string", description: "The city to get weather for" },
    },
    required: ["city"],
  },
  run: ({ city }) => `Weather in ${city}: 95F, sunny`,
});

const getForecast = betaTool({
  name: "get_forecast",
  description: "Get the 3-day weather forecast for a city.",
  inputSchema: {
    type: "object",
    properties: {
      city: { type: "string", description: "The city to get the forecast for" },
    },
    required: ["city"],
  },
  run: ({ city }) =>
    `3-day forecast for ${city}: Day 1: 95F sunny, Day 2: 89F partly cloudy, Day 3: 78F rain`,
});

const runner = client.beta.messages.toolRunner({
  model: "claude-sonnet-5",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content:
        "I'm packing for a three-day trip to Denver. What's the weather today and over the next few days?",
    },
  ],
  tools: [getWeather, getForecast],
});

// Returns the final assistant message after all the tool ping-pong has settled
const finalMessage = await runner.runUntilDone();

for (const block of finalMessage.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}
