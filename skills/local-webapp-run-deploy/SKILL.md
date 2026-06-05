---
name: local-webapp-run-deploy
description: Restart, verify, package, and deploy local web apps for Michael Song. Use when a localhost/127.0.0.1 page cannot open, a start button does not launch the browser, the user worries the site stops after reboot, or the user asks to deploy/push a local project to GitHub.
---

# Local Web App Run Deploy

## Triage

Use this skill for recurring local app startup, browser launch, persistence, and GitHub deployment requests.

1. Identify the project root and framework from files such as `package.json`, `vite.config.*`, `next.config.*`, `src/`, `app/`, or static HTML.
2. Check whether dependencies are installed and whether a server is already running.
3. Run the correct dev/preview command from the project root. If the port is occupied, inspect the process and choose a safe alternative unless the user asks to stop it.
4. Open or verify the exact URL the app reports. For local frontend work, use the in-app browser/browser verification when available.
5. If the user says rebooting breaks the site, explain that dev servers stop when the computer restarts and provide a practical persistent path.

## Persistent Startup Options

Choose the lightest durable option that fits the project:

- Add clear npm scripts such as `dev`, `build`, `preview`, and a Windows-friendly start script.
- Create a shortcut or documented command if the user only needs local personal use.
- Use a Windows scheduled task or startup script only when the user wants automatic startup after reboot.
- Deploy to GitHub/Vercel/static hosting when the user wants others to download or access it without their local server.

## GitHub Deployment

When deploying to GitHub:

1. Inspect git status and remote configuration.
2. Avoid committing unrelated user changes unless requested.
3. Build the app before publishing.
4. Commit with a concise message describing the delivered feature.
5. Push to the requested repository/branch.
6. Explain whether GitHub alone is source hosting or whether GitHub Pages/Vercel/another host is needed for a live web URL.

## Browser Launch Buttons

When a local app has a "start-*-game" or similar launch button:

- Check event handlers, route paths, and button type/default form behavior.
- Verify the browser navigation target exists.
- Test by clicking the button in the browser, not only by reading code.

## Completion

Report the URL, the command used to start it, whether it will survive reboot, and any deployment/build status.
