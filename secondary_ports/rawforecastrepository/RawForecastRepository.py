import abc


class RawForecastRepository(object):

    @abc.abstractmethod
    def upload_raw_reading_list(self, for_run):
        raise NotImplementedError(f"Class {self.__class__.__name__} doesnt implement upload_raw_reading_list method.")

    @abc.abstractmethod
    def upload_compiled_forecast_file_of_location_id_and_day_id(self, forecast_file, measurement_location_id, day_id):
        raise NotImplementedError(f"Class {self.__class__.__name__} doesnt implement upload_compiled_forecast_file_of_location_id_and_day_id method.")

    @abc.abstractmethod
    def prepare_raw_forecasts_of_locations_for_base_hour(self, measurement_location_ids, targetedCrawlIDOfBaseHour):
        raise NotImplementedError(f"Class {self.__class__.__name__} doesnt implement prepare_raw_forecasts_of_locations_for_base_hour method.")

    @abc.abstractmethod
    def prepare_forecasts_of_location_id_and_crawl_id_and_distance(self, measurement_location_id, crawlID, distance):
        raise NotImplementedError(f"Class {self.__class__.__name__} doesnt implement prepare_forecasts_of_location_id_and_crawl_id_and_distance method.")

    @abc.abstractmethod
    def prepare_forecasts_for_all_possible_distances_of_location_id_and_crawl_id(self, measurement_location_id, crawl_id):
        raise NotImplementedError(f"Class {self.__class__.__name__} doesnt implement prepare_forecasts_for_all_possible_distances_of_location_id_and_crawl_id method.")
