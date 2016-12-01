help:
	@echo "Help on Makefile targets"
	@echo ""
	@echo " * makemessages: Make i18n messages"
	@echo " * compilemessages: Compile .po into .mo"

makemessages:
	django-admin.py makemessages --all

compilemessages:
	django-admin.py compilemessages
