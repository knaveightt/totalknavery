#OBJS specifies which files to compile as part of the project
OBJS = _gentags.py

#CC specifies which compiler we are using
cc = python

#Default Target
all : rebuild

#Target a release build
clean :
	rm tags/*.html

#Force rebuilding of tags
rebuild : update
	$(cc) $(OBJS)

update :
	cp ~/Documents/global/projects.yaml _data/projects.yaml
