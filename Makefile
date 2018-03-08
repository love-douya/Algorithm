.PHONY: clean All

All:
	@echo "----------Building project:[ Dijkstra_List - Debug ]----------"
	@cd "Dijkstra_List" && "$(MAKE)" -f  "Dijkstra_List.mk"
clean:
	@echo "----------Cleaning project:[ Dijkstra_List - Debug ]----------"
	@cd "Dijkstra_List" && "$(MAKE)" -f  "Dijkstra_List.mk" clean
