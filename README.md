# Proyecto RII 3: Robots Inteligentes - Grupo 11

Este repositorio contiene el paquete de ROS 2 Humble `g11_prii3_turtlesim` para el control autónomo y trazado del número 11 en el simulador `turtlesim`.

## Requisitos previos

- **Sistema Operativo:** Ubuntu 22.04 LTS
- **Distribución de ROS 2:** ROS 2 Humble Hawksbill (`ros-humble-desktop`)
- **Herramientas de construcción:** `colcon`

## Estructura del repositorio

```text
g11_prii3_ws/
└── src/
    └── g11_prii3_turtlesim/
        ├── g11_prii3_turtlesim/
        │   ├── __init__.py
        │   └── turtle_drawer.py
        ├── launch/
        │   └── draw.launch.py
        ├── package.xml
        ├── setup.cfg
        └── setup.py
```

## Instrucciones de clonación y compilación

1. Clonar el repositorio en la carpeta deseada:
   ```bash
   git clone https://github.com/dmortrio/g11_prii3.git ~/g11_prii3_ws
   cd ~/g11_prii3_ws
   ```

2. Compilar el paquete:
   ```bash
   colcon build --packages-select g11_prii3_turtlesim
   ```

3. Cargar las variables de entorno del espacio de trabajo:
   ```bash
   source /opt/ros/humble/setup.bash
   source install/setup.bash
   ```

## Ejecución

Para iniciar el simulador `turtlesim` y el nodo autónomo de dibujo en un único comando mediante el archivo *launch*:

```bash
ros2 launch g11_prii3_turtlesim draw.launch.py
```

## Servicios ROS implementados

El nodo expone servicios estándar `std_srvs/srv/Trigger` para interactuar con la ejecución:

- **Detener:**
  ```bash
  ros2 service call /detener std_srvs/srv/Trigger "{}"
  ```
- **Reanudar:**
  ```bash
  ros2 service call /reanudar std_srvs/srv/Trigger "{}"
  ```
- **Reiniciar:**
  ```bash
  ros2 service call /reiniciar std_srvs/srv/Trigger "{}"
  ```
