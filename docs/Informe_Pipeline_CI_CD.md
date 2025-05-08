# Informe de Funcionamiento del Pipeline CI/CD

Este documento describe el funcionamiento de un pipeline CI/CD implementado con **GitHub Actions**. El propósito de este flujo es automatizar la integración y entrega continua del código fuente de un proyecto Python, garantizando que el código cumpla ciertos estándares de calidad y que los errores sean detectados de manera anticipada.

## Nombre del Pipeline

```yaml
name: CI/CD Pipeline
```

## Desencadenadores (`on`)

El pipeline se ejecuta automáticamente en dos situaciones:

- **`push`**: Cuando se realiza un push al branch `main`.
- **`pull_request`**: Cuando se crea o actualiza un pull request hacia el branch `main`.

Esto garantiza que cualquier cambio en la rama principal sea validado de forma automática antes de integrarse o desplegarse.

## Job Principal: `build-test-analyze`

Este job define una serie de pasos que se ejecutan sobre una máquina virtual basada en Ubuntu.

```yaml
runs-on: ubuntu-latest
```

### Pasos del Job

1. ### Checkout del Código

   ```yaml
   - name: Checkout code
     uses: actions/checkout@v3
   ```

   Descarga el repositorio en la máquina virtual para que el código esté disponible en los siguientes pasos.

2. ### Configuración de Python

   ```yaml
   - name: Set up Python
     uses: actions/setup-python@v4
     with:
       python-version: '3.10'
   ```

   Establece Python 3.10 como la versión predeterminada para ejecutar scripts y comandos en el entorno.

3. ### Instalación de Dependencias

   ```yaml
   - name: Install dependencies
     run: |
       python -m pip install --upgrade pip
       pip install -r requirements.txt
   ```

   - Actualiza `pip` a la última versión.
   - Instala todas las dependencias listadas en `requirements.txt`.

4. ### Verificación de Compilación

   ```yaml
   - name: Check Compilation
     run: |
       python -m compileall src
   ```

   Compila todos los archivos Python en el directorio `src` para verificar que no haya errores de sintaxis.

5. ### Análisis Estático con Pylint

   ```yaml
   - name: Run Pylint
     run: |
       pylint $(git ls-files '*.py') || true
   ```

   Ejecuta **Pylint** sobre todos los archivos `.py` del repositorio. El comando `|| true` evita que errores de linting detengan el pipeline, permitiendo que continúe incluso si se detectan problemas de estilo o advertencias.

6. ### Envío del Reporte de Cobertura a Codacy

   ```yaml
   - name: Send Coverage to Codacy
     run: |
       python-codacy-coverage -r coverage.xml || true
     env:
       CODACY_PROJECT_TOKEN: ${{ secrets.CODACY_PROJECT_TOKEN }}
   ```

   - Envia el reporte de cobertura (archivo `coverage.xml`) a **Codacy** para análisis de calidad de código.
   - Utiliza el token secreto `CODACY_PROJECT_TOKEN`, almacenado de forma segura en los **secrets** del repositorio.
   - Al igual que con Pylint, el uso de `|| true` asegura que el pipeline no falle si ocurre un error durante el envío.

---

## Conclusión

Este pipeline garantiza que cualquier modificación al código:

- Sea validada automáticamente mediante análisis estático y verificación de sintaxis.
- Mantenga la integridad del proyecto al asegurar que el código sea compilable.
- Sea analizada por herramientas externas (como Codacy) para obtener métricas de calidad y cobertura.

La automatización de estas tareas es fundamental para mantener la calidad y la estabilidad del proyecto a medida que evoluciona.