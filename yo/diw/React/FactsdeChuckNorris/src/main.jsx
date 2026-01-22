/**
 * @fileoverview Punto de entrada de la aplicación React
 * Este archivo configura e inicializa la aplicación React en el DOM
 */

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';

/**
 * Inicializa y renderiza la aplicación React
 * 
 * Proceso:
 * 1. Obtiene el elemento root del DOM (usualmente un div con id="root")
 * 2. Crea la raíz de React usando createRoot
 * 3. Renderiza el componente App envuelto en StrictMode
 * 
 * StrictMode es un componente de desarrollo que:
 * - Resalta posibles problemas en la aplicación
 * - Ejecuta ciertos checks y warnings en desarrollo
 * - No tiene impacto en la compilación final de producción
 */
createRoot(document.getElementById('root')).render(
  // StrictMode: Componente que activa verificaciones adicionales en desarrollo
  <StrictMode>
    {/* Componente principal de la aplicación */}
    <App />
  </StrictMode>,
)
