	FROM python:3.9.7
	
	RUN mkdir -p /usr/src/app/
	WORKDIR /usr/src/app
	
	COPY . /usr/src/app/
#	RUN python -m pip install --upgrade pip
	#RUN /usr/local/bin/python -m pip install --upgrade pip
	RUN pip install --no-cache-dir -r requirements.txt




	EXPOSE 8080	
		
#	CMD ["python", "app.py"]
	CMD ["python", "bot_telegram.py"]
	
	


