__import__("importlib").import_module("http.server").HTTPServer(('', 8080, [(lambda x: print("building handler..."))(None),handler := __import__("importlib").import_module("http.server").SimpleHTTPRequestHandler, [avatar := "data:image/webp;base64,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"],[handle_path := { "/hello": {"type": "text/plain","content": "Hello world!"},"/": {"type": "text/html","content": f'{(page := lambda pagename, inner: "<!DOCTYPE html><html><head><meta charset=\"UTF-8\" /><title>hi! im aenri &lt;3</title><script src=\"" + pagename + ".js\"></script><link rel=\"stylesheet\" href=\"" + pagename + ".css\"><link rel=\"stylesheet\" href=\"root.css\"></head><body><div id=\"root\">" + inner + "</div></body></html>")("index", "<h1>hi! im aenri &lt;3</h1><p id=\"about-line\">meow/kit/she/it | 18 | professional cat, amateur developer</p><p>this website is actually not a static file! it runs entirely on one line of python code :D</p><div id=\"links\"> <div><a href=\"/projects\"> projects </a></div> <div><a href=\"\"> connections </a></div> <div><a href=\"data:text/html;base64,PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PHRpdGxlPmtpbGwgeW91IGFyZSBzZWxmPC90aXRsZT48L2hlYWQ+PGJvZHk+PGgxPmtpbGwgeW91cnNlbGY8L2gxPjxoMj5ub3c8L2gyPjwvYm9keT48L2h0bWw+\" target=\"_blank\"> this button fucking kills you </a></div> </div>")}'}, "/main.js": {"type": "text/javascript", "content": "setTimeout(() => {document.querySelector(\"#kys\").addEventListener(\"click\", function() { window.alert(\"Hello World!\"); });background()}, 50);function background() {let text = fetch(\"main.py\");document.getElementById(\"code-background\").innerHTML = text;document.getElementById(\"code-background\").style.whiteSpace = \"pre-wrap\";document.getElementById(\"code-background\").classList.add(\"background-ready\")}"}, "/root.css": {"type": "text/css", "content": "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800;900&display=swap');:root {--ctp-rosewater: 245, 224, 220;--ctp-flamingo: 242, 205, 205;--ctp-pink: 245, 194, 231;--ctp-mauve: 203, 166, 247;--ctp-red: 243, 139, 168;--ctp-maroon: 235, 160, 172;--ctp-peach: 250, 179, 135;--ctp-yellow: 249, 226, 175;--ctp-green: 166, 227, 161;--ctp-teal: 148, 226, 213;--ctp-sky: 137, 220, 235;--ctp-sapphire: 116, 199, 236;--ctp-blue: 137, 180, 250;--ctp-lavender: 180, 190, 254;--ctp-text: 205, 214, 244;--ctp-subtext1: 186, 194, 222;--ctp-subtext0: 166, 173, 200;--ctp-overlay2: 147, 153, 178;--ctp-overlay1: 127, 132, 156;--ctp-overlay0: 108, 112, 134;--ctp-surface2: 88, 91, 112;--ctp-surface1: 69, 71, 90;--ctp-surface0: 49, 50, 68;--ctp-crust: 17, 17, 27;--ctp-mantle: 24, 24, 37;--ctp-base: 30, 30, 46;}body {background-color: rgb(var(--ctp-base));color: rgb(var(--ctp-text));font-family: 'Inter', sans-serif;font-weight: 400;user-select: none;position: absolute;top: 0;left: 0;width: 100%;height: 100%;padding: 0%;margin: 0%;display: flex;flex-direction: column;justify-content: center;align-items: center;}div#root { display: flex;flex-direction: column;justify-content: center;align-items: center;margin: 0.5rem;/* shows in center of page, surface color backgrounf */background-color: rgb(var(--ctp-surface1));border-radius: 0.5rem;padding: 0.5rem;box-shadow: 0 0 1rem 0.5rem rgba(var(--ctp-surface0), 0.5);} #back-chevron {width: 1em; height: 1em; fill: rgb(var(--ctp-text));} #back-chevron path {stroke-width: 4;}"}, "/projects": {"type": "text/html", "content": f"{page("projects", f"<h1><a href=\"/\"><svg id=\"back-chevron\" xmlns=\"http://www.w3.org/2000/svg\" height=\"1em\" viewBox=\"0 0 320 512\"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d=\"M34.52 239.03L228.87 44.69c9.37-9.37 24.57-9.37 33.94 0l22.67 22.67c9.36 9.36 9.37 24.52.04 33.9L131.49 256l154.02 154.75c9.34 9.38 9.32 24.54-.04 33.9l-22.67 22.67c-9.37 9.37-24.57 9.37-33.94 0L34.52 272.97c-9.37-9.37-9.37-24.57 0-33.94z\"/></svg></a>projects :D </h1> <div id=\"containers\"> {(project_container := lambda projectName, description, link, icons = []: f"<div id=\"container-item\"><h1><a href=\"{link}\" { "class=\"no-link-main\"" if not link else ""}>{projectName}</a></h1><h3>{description}</h3><div class=\"icons\">{"".join([f"<a href=\"{icon["link"]}\"><img src=\"{icon["src"]}\" /></a>" for icon in icons])}</div></div>")("bomb!", "kaboom :3", "https://www.youtube.com/watch?v=F600bVI0BOI", [{"src": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iI2NkZDZmNCI+PHBhdGggZD0iTTQ1OS4xIDUyLjRMNDQyLjYgNi41QzQ0MC43IDIuNiA0MzYuNSAwIDQzMi4xIDBzLTguNSAyLjYtMTAuNCA2LjVMNDA1LjIgNTIuNGwtNDYgMTYuOGMtNC4zIDEuNi03LjMgNS45LTcuMiAxMC40YzAgNC41IDMgOC43IDcuMiAxMC4ybDQ1LjcgMTYuOCAxNi44IDQ1LjhjMS41IDQuNCA1LjggNy41IDEwLjQgNy41czguOS0zLjEgMTAuNC03LjVsMTYuNS00NS44IDQ1LjctMTYuOGM0LjItMS41IDcuMi01LjcgNy4yLTEwLjJjMC00LjYtMy04LjktNy4yLTEwLjRMNDU5LjEgNTIuNHptLTEzMi40IDUzYy0xMi41LTEyLjUtMzIuOC0xMi41LTQ1LjMgMGwtMi45IDIuOUMyNTYuNSAxMDAuMyAyMzIuNyA5NiAyMDggOTZDOTMuMSA5NiAwIDE4OS4xIDAgMzA0UzkzLjEgNTEyIDIwOCA1MTJzMjA4LTkzLjEgMjA4LTIwOGMwLTI0LjctNC4zLTQ4LjUtMTIuMi03MC41bDIuOS0yLjljMTIuNS0xMi41IDEyLjUtMzIuOCAwLTQ1LjNsLTgwLTgwek0yMDAgMTkyYy01Ny40IDAtMTA0IDQ2LjYtMTA0IDEwNHY4YzAgOC44LTcuMiAxNi0xNiAxNnMtMTYtNy4yLTE2LTE2di04YzAtNzUuMSA2MC45LTEzNiAxMzYtMTM2aDhjOC44IDAgMTYgNy4yIDE2IDE2cy03LjIgMTYtMTYgMTZoLTh6Ii8+PC9zdmc+","link": ""}])} {project_container("RootVM", "RootVM is a JVM-like virtual machine for RootIR, it is in early stages of brainstorming/development and is planned to be built in rust/zig and will be register-based.", "https://github.com/chimera-organization/rootvm")} </div>")}"}, "/index.css": {"type": "text/css", "content": "button {background-color: rgb(var(--ctp-surface2));color: rgb(var(--ctp-text));font-family: 'Inter', sans-serif;font-weight: 400;font-size: 1.5rem;border: none;border-radius: 0.5rem;padding: 0.5rem 1rem;margin: 0.5rem;cursor: pointer;transition: all 0.2s ease-in-out;}div#links { display: flex;flex-direction: row;justify-content: center;align-items: center;margin: 0.5rem;}div#links > div { padding: 0.5rem;background-color: rgb(var(--ctp-surface1));border-radius: 0.5rem;margin: 0.5rem;cursor: pointer;transition: all 0.2s ease-in-out;}div#links > div:hover {background-color: rgb(var(--ctp-overlay1))}div#links > div > a {text-decoration: none;color: rgb(var(--ctp-text));font-family: 'Inter', sans-serif;font-weight: 400;font-size: 1.5rem;}"}, "/projects.css": {"type": "text/css", "content": "@media screen and (max-width:768px){#containers{grid-template-columns:1fr;grid-gap:10px;margin:0auto;width:90%;padding-top:50px;padding-bottom:50px;padding-left:10px;padding-right:10px;}}@media screen and (min-width:769px) and (max-width:1024px) {#root{width:70%;}#containers{grid-template-columns:1fr;grid-gap:20px;/*margin:0auto;*/width:90%;padding-top:50px;padding-bottom:50px;padding-left:10px;padding-right:10px;}}@media screen and (min-width:1025px){#root{width:70%;}#containers{grid-template-columns:1fr 1fr 1fr;grid-gap:20px;/*margin:0auto;*/width:90%;padding-top:50px;padding-bottom:50px;padding-left:10px;padding-right:10px;}}#containers{display:grid;background:rgb(var(--ctp-crust));border-radius:10px;}#container-item{background:rgb(var(--ctp-surface0));border-radius:10px;padding:10px;box-shadow:0010px0rgba(0,0,0,0.2);}#container-item a{color:rgb(var(--ctp-text));}#container-item a:not(.no-link-main){text-decoration:underline;}#container-item a:hover:not(.no-link-main){color:rgb(var(--ctp-subtext1));}#container-item div.icons{display:flex;justify-content:space-between;align-items:center;margin-top:10px;}#container-item div.icons a{color:rgb(var(--ctp-text));fill:rgb(var(--ctp-text));}#container-item div.icons a img{width:2.2em;height:2.2em;}a:has(#back-chevron){background-color:rgb(var(--ctp-surface2));border-radius:10px;padding:0.2em;margin-right:10px;line-height:0.75em;display:inline-block;transform:translateY(0.2em)}h1:has(a:has(#back-chevron)){display:flex;align-items:left;}"}}],[old_handle := handler.do_GET],[handle_item := (lambda self: (((lambda x: print(f"handling request for path: {self.path}"))(None) or 1) and not (((lambda x: (self.send_response(200) or 1) and not (print(f"in-memory hit for {self.path}") or 0) and not (self.send_header("Content-Type", handle_path[self.path]["type"]) or 0) and not (self.end_headers() or 0) and not (self.wfile.write(handle_path[self.path]["content"].encode("utf-8")) or 0))(None)) if self.path in handle_path else (lambda x: (print(f"static file got: {self.path}") or 1) and not (old_handle(self) or 0))(None)))),],(lambda h: exec("h.do_GET = handle_item", {"h":h, "handle_item":handle_item}))(handler),(lambda x: print("handler built!"))(None)])[:-1],handler).serve_forever()