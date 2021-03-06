from measurement_logger.measurement_logger import MeasurementLogger
import datetime


class FileMeasurementLogger(MeasurementLogger):
	
    def ensure_dir(self,file_path):
        import os
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
    def __init__(self, measurement_db_name, measurement_definitions, directory):
        super(FileMeasurementLogger, self).__init__(measurement_db_name, measurement_definitions)
        self.filenames = []
        self.filenames_mapping = {}
        for key in self.measurement_definitions:
            self.filenames.append(measurement_db_name + "_upi_" + key)
            self.filenames_mapping[key] = measurement_db_name + "_upi_" + key
        self.file_writers = {}
        self.directory = directory
        self.ensure_dir(self.directory)
        pass

    def log_measurement(self, name, value):
        self.log.debug("{};{}".format(datetime.datetime.now(), value))
        self.file_writers[self.filenames_mapping[name]].write("{};{}\n".format(datetime.datetime.now(), value))
        self.file_writers[self.filenames_mapping[name]].flush()
        pass

    def start_logging(self):
        for fname in self.filenames:
            self.file_writers[fname] = open(self.directory + fname, 'w')
        pass
    
    def stop_logging(self):
        for fname in self.filenames:
            self.file_writers[fname].close()
        pass
        
