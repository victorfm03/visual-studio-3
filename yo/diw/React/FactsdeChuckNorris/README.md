# 🎭 FactsdeChuckNorris - Aplicación React

Una aplicación web moderna construida con React y Vite que muestra categorías de chistes de Chuck Norris utilizando la API pública de Chuck Norris.

## 📋 Descripción

**FactsdeChuckNorris** es una aplicación interactiva que:
- ✅ Obtiene categorías de chistes desde la API de Chuck Norris
- ✅ Proporciona un selector elegante para elegir categorías
- ✅ Está completamente documentada con JSDoc
- ✅ Usa Bootstrap para una interfaz responsiva
- ✅ Implementa patrones de React modernos con hooks

## 🚀 Comenzar Rápidamente

### Requisitos previos
- Node.js 16 o superior
- npm o yarn

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/FactsdeChuckNorris.git
cd FactsdeChuckNorris

# Instalar dependencias
npm install
```

### Ejecutar en desarrollo

```bash
npm run dev
```

La aplicación estará disponible en `http://localhost:5173`

### Compilar para producción

```bash
npm run build
```

### Validar código con ESLint

```bash
npm run lint
```

### Vista previa de compilación

```bash
npm run preview
```

## 📁 Estructura del Proyecto

```
FactsdeChuckNorris/
├── src/
│   ├── App.jsx                         # Componente principal
│   ├── CategoriasChistes.jsx           # Componente selector de categorías
│   ├── main.jsx                        # Punto de entrada
│   ├── assets/                         # Recursos estáticos
├── public/                             # Archivos públicos
├── index.html                          # Archivo HTML principal
├── vite.config.js                      # Configuración de Vite
├── eslint.config.js                    # Configuración de ESLint
├── package.json                        # Dependencias y scripts
├── DOCUMENTACION.md                    # Documentación completa
├── PATRONES_Y_BUENAS_PRACTICAS.js     # Guía de mejores prácticas
├── VALIDACION_Y_LINTING.js            # Guía de validación
└── README.md                           # Este archivo
```

## 🏗️ Componentes

### App.jsx
Componente raíz que:
- Gestiona el estado de la categoría seleccionada
- Renderiza el selector de categorías
- Proporciona la estructura HTML principal

### CategoriasChistes.jsx
Componente que:
- Obtiene categorías desde la API de Chuck Norris
- Renderiza un dropdown para seleccionar categorías
- Notifica al componente padre sobre cambios
- Maneja la carga asincrónica de datos

## 📚 Documentación

El proyecto incluye documentación exhaustiva:

- **[DOCUMENTACION.md](DOCUMENTACION.md)** - Documentación técnica completa
- **[PATRONES_Y_BUENAS_PRACTICAS.js](PATRONES_Y_BUENAS_PRACTICAS.js)** - Guía de patrones y mejores prácticas
- **[VALIDACION_Y_LINTING.js](VALIDACION_Y_LINTING.js)** - Guía de validación y linting

Todos los archivos JSX incluyen:
- ✅ Bloques JSDoc detallados
- ✅ Comentarios explicativos en el código
- ✅ Ejemplos de uso
- ✅ Descripciones de parámetros y retornos

## 🔌 API Utilizada

### Chuck Norris API
- **URL:** `https://api.chucknorris.io/jokes/categories`
- **Método:** GET
- **Respuesta:** Array de strings con nombres de categorías

Ejemplo de respuesta:
```json
[
  "animal",
  "career",
  "celebrity",
  "dev",
  "explicit",
  "fashion",
  "food",
  "history"
]
```

## 🛠️ Tecnologías Utilizadas

### Runtime
- **React 19.2.0** - Librería UI
- **React DOM 19.2.0** - Renderizado en DOM

### Build Tools
- **Vite 7.2.4** - Build tool y bundler
- **@vitejs/plugin-react** - Plugin React para Vite

### Estilos
- **Bootstrap 5** - Framework CSS responsivo

### Desarrollo
- **ESLint 9.39.1** - Linter de JavaScript
- **eslint-plugin-react-hooks** - Reglas para React hooks
- **eslint-plugin-react-refresh** - Soporte para Fast Refresh

## 📖 Patrones Implementados

### Hooks React
- ✅ **useState** - Gestión de estado local
- ✅ **useEffect** - Efectos secundarios (obtención de datos)

### Manejo de datos
- ✅ **Fetch API** - Comunicación con API
- ✅ **Async/Await** - Control de promesas

### Componentes
- ✅ **Componentes funcionales** - Arquitectura moderna
- ✅ **Props drilling** - Comunicación padre-hijo
- ✅ **Callbacks** - Comunicación inversa

## 🎨 Características de Código

### Documentación JSDoc
Todos los componentes y funciones incluyen:
```javascript
/**
 * Descripción detallada
 * @component
 * @param {Type} name - Descripción
 * @returns {JSX.Element} Descripción
 * @example
 * <Componente prop="valor" />
 */
```

### Comentarios Explicativos
- Comentarios sobre estados y su propósito
- Explicación de lógica compleja
- Documentación de dependencias de hooks
- Clarificación de integraciones con APIs

### Estándares de Código
- Naming consistente (camelCase, PascalCase)
- Indentación de 2 espacios
- Comentarios antes del código
- Ejemplos de uso en JSDoc

## ✅ Validación

El proyecto incluye:
- ✅ ESLint configurado
- ✅ Documentación JSDoc completa
- ✅ Manejo de errores
- ✅ Validación de APIs

Para validar el código:
```bash
npm run lint
```

## 🚀 Mejoras Futuras

- [ ] Agregar caché para las categorías
- [ ] Implementar indicador visual de carga
- [ ] Agregar manejo de errores mejorado
- [ ] Agregar tests unitarios
- [ ] Convertir a TypeScript
- [ ] Agregar listado de chistes por categoría

## 📝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 📞 Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

---

**Última actualización:** Enero 2026
**Versión:** 1.0.0
**Mantenedor:** Tu nombre/organización
