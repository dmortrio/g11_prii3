import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen, TeleportAbsolute
from std_srvs.srv import Trigger

class TurtleDrawer(Node):
    def __init__(self):
        super().__init__('turtle_drawer')

        #Control del lapiz y turtle
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')

        # Servicios ROS
        self.srv_detener = self.create_service(Trigger, 'detener', self.cb_detener)
        self.srv_reanudar = self.create_service(Trigger, 'reanudar', self.cb_reanudar)
        self.srv_reiniciar = self.create_service(Trigger, 'reiniciar', self.cb_reiniciar)

        # pen_off: 1 = no dibuja, 0 = dibuja trazo
        self.points = [
            #PRIMER 1
            (3.0, 6.5, 0.9, 1),
            (4.0, 8.0, -1.57, 0),
            (4.0, 3.5, 0.0, 0),
            (2.8, 3.5, 0.0, 1),
            (5.2, 3.5, 0.0, 0),

            #SEGUNDO 1
            (6.5, 6.5, 0.9, 1),
            (7.5, 8.0, -1.57, 0),
            (7.5, 3.5, 0.0, 0),
            (6.3, 3.5, 0.0, 1),
            (8.7, 3.5, 0.0, 0),

            # Fin: levantar lápiz
            (8.7, 3.5, 0.0, 1)
        ]

        self.current_idx = 0
        self.state = 'INITIALIZING'
        self.timer = self.create_timer(0.4, self.loop)
        self.get_logger().info('TurtleDrawer listo.')

    def set_pen(self, off):
        if self.pen_client.service_is_ready():
            req = SetPen.Request()
            req.r = 255
            req.g = 255
            req.b = 255
            req.width = 4
            req.off = off
            self.pen_client.call_async(req)

    def teleport(self, x, y, theta):
        if self.teleport_client.service_is_ready():
            req = TeleportAbsolute.Request()
            req.x = float(x)
            req.y = float(y)
            req.theta = float(theta)
            self.teleport_client.call_async(req)

    def cb_detener(self, request, response):
        self.state = 'PAUSED'
        response.success = True
        response.message = 'Dibujo detenido.'
        self.get_logger().info('Servicio: PAUSADO')
        return response

    def cb_reanudar(self, request, response):
        if self.state == 'PAUSED':
            self.state = 'RUNNING'
            response.success = True
            response.message = 'Dibujo reanudado.'
            self.get_logger().info('Servicio: REANUDADO')
        else:
            response.success = False
            response.message = f'No está pausado (estado actual: {self.state}).'
        return response

    def cb_reiniciar(self, request, response):
        self.current_idx = 0
        self.set_pen(1)
        self.state = 'RUNNING'
        response.success = True
        response.message = 'Dibujo reiniciado.'
        self.get_logger().info('Servicio: REINICIADO')
        return response

    def loop(self):
        if self.state == 'INITIALIZING':
            if self.pen_client.service_is_ready() and self.teleport_client.service_is_ready():
                self.set_pen(1)
                self.state = 'RUNNING'
                self.get_logger().info('Servicios conectados. Iniciando trazado del 11.')
            return

        if self.state != 'RUNNING':
            return

        if self.current_idx >= len(self.points):
            self.state = 'FINISHED'
            self.set_pen(1)
            self.get_logger().info('¡Número 11 completado con éxito!')
            return

        x, y, theta, pen_off = self.points[self.current_idx]
        self.set_pen(pen_off)
        self.teleport(x, y, theta)
        self.current_idx += 1

def main(args=None):
    rclpy.init(args=args)
    node = TurtleDrawer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
