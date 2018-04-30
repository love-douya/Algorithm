.PHONY: clean All

All:
	@echo "----------Building project:[ struct_and_class - Debug ]----------"
	@cd "struct_and_class" && "$(MAKE)" -f  "struct_and_class.mk"
clean:
	@echo "----------Cleaning project:[ struct_and_class - Debug ]----------"
	@cd "struct_and_class" && "$(MAKE)" -f  "struct_and_class.mk" clean
