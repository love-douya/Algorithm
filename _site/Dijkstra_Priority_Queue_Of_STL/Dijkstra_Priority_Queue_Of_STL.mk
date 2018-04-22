##
## Auto Generated makefile by CodeLite IDE
## any manual changes will be erased      
##
## Debug
ProjectName            :=Dijkstra_Priority_Queue_Of_STL
ConfigurationName      :=Debug
WorkspacePath          :=C:/Users/TAO/Desktop/Algorithm
ProjectPath            :=C:/Users/TAO/Desktop/Algorithm/Dijkstra_Priority_Queue_Of_STL
IntermediateDirectory  :=./Debug
OutDir                 := $(IntermediateDirectory)
CurrentFileName        :=
CurrentFilePath        :=
CurrentFileFullPath    :=
User                   :=TAO
Date                   :=13/04/2018
CodeLitePath           :=C:/CodeLite
LinkerName             :=C:/mingw/bin/g++.exe
SharedObjectLinkerName :=C:/mingw/bin/g++.exe -shared -fPIC
ObjectSuffix           :=.o
DependSuffix           :=.o.d
PreprocessSuffix       :=.i
DebugSwitch            :=-g 
IncludeSwitch          :=-I
LibrarySwitch          :=-l
OutputSwitch           :=-o 
LibraryPathSwitch      :=-L
PreprocessorSwitch     :=-D
SourceSwitch           :=-c 
OutputFile             :=$(IntermediateDirectory)/$(ProjectName)
Preprocessors          :=
ObjectSwitch           :=-o 
ArchiveOutputSwitch    := 
PreprocessOnlySwitch   :=-E
ObjectsFileList        :="Dijkstra_Priority_Queue_Of_STL.txt"
PCHCompileFlags        :=
MakeDirCommand         :=makedir
RcCmpOptions           := 
RcCompilerName         :=C:/mingw/bin/windres.exe
LinkOptions            :=  
IncludePath            :=  $(IncludeSwitch). $(IncludeSwitch). 
IncludePCH             := 
RcIncludePath          := 
Libs                   := 
ArLibs                 :=  
LibPath                := $(LibraryPathSwitch). 

##
## Common variables
## AR, CXX, CC, AS, CXXFLAGS and CFLAGS can be overriden using an environment variables
##
AR       := C:/mingw/bin/ar.exe rcu
CXX      := C:/mingw/bin/g++.exe
CC       := C:/mingw/bin/gcc.exe
CXXFLAGS :=  -g -O0 -Wall $(Preprocessors)
CFLAGS   :=  -g -O0 -Wall $(Preprocessors)
ASFLAGS  := 
AS       := C:/mingw/bin/as.exe


##
## User defined environment variables
##
CodeLiteDir:=C:\CodeLite
Objects0=$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(ObjectSuffix) 



Objects=$(Objects0) 

##
## Main Build Targets 
##
.PHONY: all clean PreBuild PrePreBuild PostBuild MakeIntermediateDirs
all: $(OutputFile)

$(OutputFile): $(IntermediateDirectory)/.d $(Objects) 
	@$(MakeDirCommand) $(@D)
	@echo "" > $(IntermediateDirectory)/.d
	@echo $(Objects0)  > $(ObjectsFileList)
	$(LinkerName) $(OutputSwitch)$(OutputFile) @$(ObjectsFileList) $(LibPath) $(Libs) $(LinkOptions)

MakeIntermediateDirs:
	@$(MakeDirCommand) "./Debug"


$(IntermediateDirectory)/.d:
	@$(MakeDirCommand) "./Debug"

PreBuild:


##
## Objects
##
$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(ObjectSuffix): Dijkstra_Priority_Queue_Of_STL.cpp $(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(DependSuffix)
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/TAO/Desktop/Algorithm/Dijkstra_Priority_Queue_Of_STL/Dijkstra_Priority_Queue_Of_STL.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(DependSuffix): Dijkstra_Priority_Queue_Of_STL.cpp
	@$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) -MG -MP -MT$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(ObjectSuffix) -MF$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(DependSuffix) -MM Dijkstra_Priority_Queue_Of_STL.cpp

$(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(PreprocessSuffix): Dijkstra_Priority_Queue_Of_STL.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/Dijkstra_Priority_Queue_Of_STL.cpp$(PreprocessSuffix) Dijkstra_Priority_Queue_Of_STL.cpp


-include $(IntermediateDirectory)/*$(DependSuffix)
##
## Clean
##
clean:
	$(RM) -r ./Debug/


