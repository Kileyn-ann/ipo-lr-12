
class Vehicle:#Создаём класс
    def __init__(self, capacity):#Создаём метод 
        self.vehicle_id = vehicle_id  # Уникальный идентификатор
        self.capacity = capacity  # Грузоподъемность в тоннах
        self.current_load = 0  # Текущая загрузка
        self.clients_list = []  # Список клиентов, чьи грузы загружены

    def load_cargo(self, client):#Метод для увеличения загрузки на cargo_weight из объекта client
    
        if not hasattr(client, 'cargo_weight'):  # Проверка типа клиента 
            raise TypeError("Объект не содержит атрибут 'cargo_weight'.")

   
        if not isinstance(client.cargo_weight, (int, float)):# Проверка, что cargo_weight — число
            raise TypeError("Атрибут 'cargo_weight' должен быть числом.")
        
        
        if self.current_load + client.cargo_weight > self.capacity:# Проверка на превышение грузоподъемности
            raise ValueError("Перевышена грузоподъемность транспортного средства.")
        
        
        self.current_load += client.cargo_weight# Обновляем текущую нагрузку и добавляем клиента
        self.clients_list.append(client)

    def __str__(self):#Магический метод
        return (f"Vehicle ID: {self.vehicle_id}\n"
                f"Capacity: {self.capacity} tons\n"
                f"Current load: {self.current_load} tons")
