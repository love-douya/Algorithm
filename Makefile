.PHONY: clean All

All:
	@echo "----------Building project:[ Dijkstra_Priority_Queue_Of_STL - Debug ]----------"
	@cd "Dijkstra_Priority_Queue_Of_STL" && "$(MAKE)" -f  "Dijkstra_Priority_Queue_Of_STL.mk"
clean:
	@echo "----------Cleaning project:[ Dijkstra_Priority_Queue_Of_STL - Debug ]----------"
	@cd "Dijkstra_Priority_Queue_Of_STL" && "$(MAKE)" -f  "Dijkstra_Priority_Queue_Of_STL.mk" clean
