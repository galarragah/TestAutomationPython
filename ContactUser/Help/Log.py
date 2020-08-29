import logging as log



class Logs:

    def __init__(self):

        #self.message = "PASO POR AQUI"
        #self.fail_message = "FALLO POR AQUI"
        #self.pass_message = "PASO POR AQUI"
        self.log_file = "C:\\Users\\hgalarraga\\Desktop\\ProyectoAutomation\\ContactUser\\Logs\\log.txt"

    def message_logs(self, mensaje):
        if mensaje == True:
            self.pass_message = "PASO POR AQUI"
            return self.pass_message
        else:
            self.fail_message = "FALLO POR AQUI"
            return self.fail_message





    def log(self, level, mensaje):
        log.basicConfig(level=log.INFO, filename=self.log_file, filemode='a',
                        format="%(asctime)-12s%(levelname)s %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S ")

        if level == "INFO":
            log.info(mensaje)
        if level == "WARNING":
            log.warning(self.message)
        if level == "ERROR":
            log.error(self.message)
        if level == "CRITICAL":
            log.critical(self.message)