help:
	@echo "Help on Makefile targets"
	@echo ""
	@echo " * makemessages: Make i18n messages"
	@echo " * compilemessages: Compile .po into .mo"
	@echo " * test: Run all the tests"
	@echo " * loaddata: Load all data"

makemessages:
	django-admin.py makemessages --all

compilemessages:
	django-admin.py compilemessages

test:
	cd ..; DJANGO_SETTINGS_MODULE=settings django-admin.py test beers

loaddata:
	cd ..; DJANGO_SETTINGS_MODULE=settings django-admin.py loaddata data notabeer
