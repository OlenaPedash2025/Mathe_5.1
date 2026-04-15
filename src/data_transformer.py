class DataTransformer:
    @staticmethod
    def transform_to_db_format(raw_data):
        prepared_data = []
        for item in raw_data:
            name = item.get("name")
            vector = item.get("vector", [])
            if len(vector) != 4:
                print(f"Skipping {name}: Expected 4 dimensions, got {len(vector)}")
                continue
            prepared_data.append((name, *vector))
            # (name, vector[0], vector[1], vector[2], vector[3])
        return prepared_data
