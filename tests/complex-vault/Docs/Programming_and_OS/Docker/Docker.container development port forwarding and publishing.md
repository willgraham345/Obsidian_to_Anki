---
type: note
---
# Background
Containers are separate environments, so accessing services, servers, or other resources require "forwarding" or "publishing" the port to your host. 
- You can either configure your container to expose these ports or just forward them temporarily. 

# Usage
## Always forwarding a port
Edit `devcontainer.json`
```json
"forwardPorts": [3000, 3001]
```
- Reload/reopen the window

## Temporarily forward a port
**Forward a Port** command from command palette
![[Pasted image 20240403153342.png]]
- After selecting a port, a notification will tell you the localhost port you should use to access the port in the container. 
- If you forwarded an HTTP server listening on port 3000, the notification may tell you that it was mapped to port 4123 on localhost. You can then connect this remote HTTP server using `http://localhost:4123`

## Publishing a Port
Docker has the concept of "publishing" ports when the container is created. Published ports behave very much like ports you make available to your local network. If your application only accepts calls from `localhost`, it will reject connections from published ports just as your local machine would for network calls. Forwarded ports, on the other hand, actually look like `localhost` to the application. Each can be useful in different situations.

To publish a port, you can:

1. **Use the appPort property:** If you reference an image or Dockerfile in `devcontainer.json`, you can use the `appPort` property to publish ports to the host.
    
    ```
    "appPort": [ 3000, "8921:5000" ]
    ```
    
2. **Use the Docker Compose ports mapping:** The [ports mapping](https://docs.docker.com/compose/compose-file#ports) can easily be added your `docker-compose.yml` file to publish additional ports.
    
    ```
    ports:
    - "3000"
    - "8921:5000"
    ```
    

In each case, you'll need to rebuild your container for the setting to take effect. You can do this by running the **Dev Containers: Rebuild Container** command in the Command Palette (F1) when you are connected to the container.