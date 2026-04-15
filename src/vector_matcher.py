import math
from data_provider import JSONDataProvider
from database_manager import create_database, fetch_data

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
    print("Creating and populating the database...")
    create_database()
    print("\nFetching data from database...")   
    data = fetch_data('my_database.db')
    for name, vector in data.items():
        print(f"{name}: {vector}")
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


   
        
