document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('ecobici-form');
    const predictionElement = document.querySelector('.prediccion');
  
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      const formData = {
        mes_origen: parseInt(document.getElementById('mes-origen').value),
        dia_semana_origen: parseInt(document.getElementById('dia-semana-origen').value),
        quincena: parseInt(document.getElementById('quincena').value),
        bici_model: parseInt(document.getElementById('bici-model').value),
        categoria_edad: parseInt(document.getElementById('categoria-edad').value),
        cat_tiempo_recorrido: parseInt(document.getElementById('cat-tiempo-recorrido').value),
        cat_hora_origen: parseInt(document.getElementById('cat-hora-origen').value),
        codigo_estacion_nombre: parseInt(document.getElementById('codigo-estacion-nombre').value)
      };
  
      try {
        const response = await fetch('http://127.0.0.1:8000/predict/', {
          method: 'POST',
          body: JSON.stringify(formData),
          headers: {
            'Content-Type': 'application/json'
          }
        });
  
        if (response.ok) {
          const data = await response.json();
          predictionElement.textContent = data.prediction;
        } else {
          predictionElement.textContent = 'Error al obtener la predicción';
        }
      } catch (error) {
        console.error(error);
        predictionElement.textContent = 'Error al obtener la predicción';
      }
    });
  });
  