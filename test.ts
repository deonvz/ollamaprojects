import { Ollama } from "ollama";
// THis typescript file shows how instructions can be send as a Agent and respective model, which then changes its characte and answers
const ollama = new Ollama();
const responses = await ollama.chat(
{
    model: 'qwen:1.8b', // select a model you have installed already
    messages: [
    { role: "system", content: "You are a helpful AI Assistant. Always answer in English."},
    { role: "user", content: "why is the sky blue?"}
    ],
    stream: true
    }
)    
// loop thru async generator and print each response to console
for await (const r of responses) {
console.log (r.message.content) ;
};