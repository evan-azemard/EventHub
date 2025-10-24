import app from "./app";
import { env } from "./config/env";

console.log("Démarrage du serveur...");
console.log(`PORT: ${env.PORT}, HOST: ${env.HOST}, NODE_ENV: ${env.NODE_ENV}`);

app.listen(env.PORT, env.HOST, () => {
  console.log(`Server is running on http://${env.HOST}:${env.PORT}`);
});
