import math
from data_provider import JSONDataProvider
from data_transformer import DataTransformer
from database_manager import DatabaseManager
class VectorMatcher:
    def __init__(self, data):
        self.supplies = data
        
    def euclidean_distance(self, v1, v2):
        """Calculates the absolute distance (ruler)."""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))
        # return math.dist(v1, v2)
    
    def cosine_similarity(self, v1, v2):
        """Calculates the structural similarity (angle)."""
        dot_product = sum(a * b for a, b in zip(v1, v2))
        norm_v1 = math.sqrt(sum(a**2 for a in v1))
        norm_v2 = math.sqrt(sum(b**2 for b in v2))
        if norm_v1 == 0 or norm_v2 == 0:
            return 0.0  # Avoid division by zero
        return dot_product / (norm_v1 * norm_v2)
    
    def run_analysis(self, query_vector):
        results = []
        for name, vector in self.supplies.items():
            distance = self.euclidean_distance(query_vector, vector)
            similarity = self.cosine_similarity(query_vector, vector)
            results.append((name, distance, similarity))
        return results
    
    
if __name__ == "__main__":
    # Load data
    raw_data = JSONDataProvider.load_from_file("data/data.json")
    if raw_data is None:
        print("No data loaded. Exiting.")
        exit(1)
    # Transform data
    transformer = DataTransformer()
    prepared_data = transformer.transform_to_db_format(raw_data)
    # Create and populate database
    db_manager = DatabaseManager('my_database.db')
    db_manager.create_database(prepared_data)
    # Fetch data from database
    print("\nFetching data from database...")   
    data = db_manager.fetch_all_suppliers()
    for name, vector in data.items():
        print(f"{name}: {vector}")
    # Run vector matching analysis
    matcher = VectorMatcher(data)
    query_vector = JSONDataProvider.load_from_file("data/query.json")
    if isinstance(query_vector, dict) and "target_profile" in query_vector:
        query_vector = query_vector["target_profile"]
    else:
        query_vector = [5.0, 5.0, 5.0, 5.0]
        print("Using default target profile.")

    print(f"Target Profile: {query_vector}\n")
    
    analysis_results = matcher.run_analysis(query_vector)
    
    for name, distance, similarity in analysis_results:
        print(f"{name}: Distance = {distance:.3f}, Similarity = {similarity:.3f}")  


   
        
