from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Leer el archivo HTML existente
    with open('amor.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Añadir el script de lluvia de corazones
    rain_script = """
    <script>
    // Lluvia de Corazones Amarillos
    class HeartRain {
        constructor() {
            this.hearts = [];
            this.colors = ['#FFD700', '#FFA500', '#FF69B4', '#FFFF00'];
            this.init();
        }
        
        init() {
            this.container = document.createElement('div');
            this.container.id = 'heartRainContainer';
            this.container.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 1;
            `;
            document.body.appendChild(this.container);
            this.startRain();
        }
        
        createHeart() {
            const heart = document.createElement('div');
            heart.innerHTML = '💛';
            heart.style.cssText = `
                position: absolute;
                left: ${Math.random() * 100}%;
                top: -50px;
                font-size: ${Math.random() * 20 + 15}px;
                color: ${this.colors[Math.floor(Math.random() * this.colors.length)]};
                animation: fall ${Math.random() * 3 + 2}s linear;
                opacity: ${Math.random() * 0.5 + 0.5};
            `;
            
            this.container.appendChild(heart);
            
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 5000);
        }
        
        startRain() {
            setInterval(() => {
                this.createHeart();
            }, 300);
        }
    }
    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fall {
            to {
                transform: translateY(100vh) rotate(360deg);
            }
        }
    `;
    document.head.appendChild(style);
    
    document.addEventListener('DOMContentLoaded', () => {
        new HeartRain();
    });
    </script>
    """
    
    html_content = html_content.replace('</body>', rain_script + '</body>')
    return html_content

if __name__ == '__main__':
    print("🌧️ Servidor de lluvia de corazones amarillos iniciado!")
    print("📱 Abre tu navegador en: http://localhost:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)
