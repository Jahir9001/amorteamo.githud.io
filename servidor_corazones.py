from flask import Flask, render_template_string, jsonify
import random
import math
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Leer el archivo HTML existente
    with open('amor.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Añadir el script de lluvia de corazones mejorada
    rain_script = """
    <script>
    // Lluvia de Corazones Amarillos Mejorada
    class HeartRain {
        constructor() {
            this.hearts = [];
            this.maxHearts = 100;
            this.colors = ['#FFD700', '#FFA500', '#FF69B4', '#FF1493', '#FFFF00'];
            this.init();
        }
        
        init() {
            // Crear contenedor para los corazones
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
            
            // Iniciar la lluvia
            this.startRain();
            
            // Añadir control manual
            this.addControls();
        }
        
        createHeart() {
            const heart = document.createElement('div');
            heart.innerHTML = ['❤️', '💛', '💕', '💖', '💝'][Math.floor(Math.random() * 5)];
            heart.style.cssText = `
                position: absolute;
                left: ${Math.random() * 100}%;
                top: -50px;
                font-size: ${Math.random() * 20 + 15}px;
                color: ${this.colors[Math.floor(Math.random() * this.colors.length)]};
                animation: fall ${Math.random() * 3 + 2}s linear infinite;
                opacity: ${Math.random() * 0.5 + 0.5};
                filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.5));
            `;
            
            // Animación de balanceo
            const swayAmount = Math.random() * 100 - 50;
            heart.style.animation += `, sway ${Math.random() * 2 + 1}s ease-in-out infinite`;
            
            this.container.appendChild(heart);
            this.hearts.push(heart);
            
            // Eliminar corazón después de la animación
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
                const index = this.hearts.indexOf(heart);
                if (index > -1) {
                    this.hearts.splice(index, 1);
                }
            }, 5000);
        }
        
        startRain() {
            // Crear corazones iniciales
            for (let i = 0; i < 20; i++) {
                setTimeout(() => this.createHeart(), i * 200);
            }
            
            // Continuar la lluvia
            this.rainInterval = setInterval(() => {
                if (this.hearts.length < this.maxHearts) {
                    this.createHeart();
                }
            }, 300);
        }
        
        addControls() {
            // Botón de control
            const controlBtn = document.createElement('button');
            controlBtn.innerHTML = '🌧️ Lluvia de Amor';
            controlBtn.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: linear-gradient(135deg, #FFD700, #FFA500);
                color: #000;
                border: none;
                padding: 15px 20px;
                border-radius: 25px;
                font-weight: bold;
                cursor: pointer;
                z-index: 10000;
                box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3);
                transition: all 0.3s ease;
            `;
            
            controlBtn.addEventListener('click', () => {
                this.burst();
            });
            
            controlBtn.addEventListener('mouseenter', () => {
                controlBtn.style.transform = 'scale(1.1)';
                controlBtn.style.boxShadow = '0 8px 20px rgba(255, 215, 0, 0.4)';
            });
            
            controlBtn.addEventListener('mouseleave', () => {
                controlBtn.style.transform = 'scale(1)';
                controlBtn.style.boxShadow = '0 5px 15px rgba(255, 215, 0, 0.3)';
            });
            
            document.body.appendChild(controlBtn);
        }
        
        burst() {
            // Crear explosión de corazones
            for (let i = 0; i < 50; i++) {
                setTimeout(() => this.createHeart(), i * 50);
            }
        }
        
        stop() {
            clearInterval(this.rainInterval);
        }
    }
    
    // Añadir animaciones CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fall {
            to {
                transform: translateY(100vh) rotate(360deg);
            }
        }
        
        @keyframes sway {
            0%, 100% { transform: translateX(0); }
            50% { transform: translateX(50px); }
        }
    `;
    document.head.appendChild(style);
    
    // Iniciar la lluvia cuando la página cargue
    document.addEventListener('DOMContentLoaded', () => {
        window.heartRain = new HeartRain();
    });
    </script>
    """
    
    # Insertar el script antes del cierre del body
    html_content = html_content.replace('</body>', rain_script + '</body>')
    
    return html_content

@app.route('/burst')
def burst():
    """Endpoint para crear explosión de corazones"""
    return jsonify({'status': 'burst triggered'})

if __name__ == '__main__':
    print("🌧️ Iniciando servidor de lluvia de corazones amarillos...")
    print("📱 Abre tu navegador en: http://localhost:5000")
    print("💛 Disfruta de la lluvia de amor para tu novia!")
    app.run(debug=True, host='0.0.0.0', port=5000)
