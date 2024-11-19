1. FROM python
2. RUN git clone https://github.com/user_name/repository_address.git
3. ENV COOL_PORT 8080
4. ENV COOL_IP 0.0.0.0
5. RUN mkdir logs
6. ENV COOL_LOG logs
7. RUN mkdir /usr/share/cool-app
8. RUN echo "Test page" > /usr/share/cool-app/cool-text.txt
9. EXPOSE 8080/tcp
10. CMD ["pytest", "-v"]