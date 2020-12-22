import os, sys, time
from colorama import Fore
from colorama import init as colorama_init

Verbose = False
Total_Removed = 0

Main_Colour = Fore.LIGHTGREEN_EX
Secondary_Colour = Fore.WHITE

Log_Locations = ["/var/log/lastlog", "/var/log/alternatives.log", "/var/log/messages", "/var/log/warn", "/var/log/wtmp", "/var/log/poplog", "/var/log/qmail", "/var/log/smtpd", "/var/log/telnetd", "/var/log/secure", "/var/log/auth", "/var/log/auth.log", "/var/log/cups/access_log", "/var/log/cups/error_log", "/var/log/thttpd_log", "/var/log/spooler", "/var/spool/tmp", "/var/spool/errors", "/var/spool/locks", "/var/log/nctfpd.errs", "/var/log/acct", "/var/apache/log", "/var/apache/logs", "/usr/local/apache/log", "/usr/local/apache/logs", "/usr/local/www/logs/thttpd_log", "/var/log/news", "/var/log/news/news", "/var/log/news.all", "/var/log/news/news.all", "/var/log/news/news.crit", "/var/log/news/news.err", "/var/log/news/news.notice", "/var/log/news/suck.err", "/var/log/news/suck.notice", "/var/log/xferlog", "/var/log/proftpd/xferlog.legacy", "/var/log/proftpd.xferlog", "/var/log/proftpd.access_log", "/var/log/httpd/error_log", "/var/log/httpsd/ssl_log", "/var/log/httpsd/ssl.access_log", "/var/adm", "/var/run/utmp", "/etc/wtmp", "/etc/utmp", "/etc/mail/access", "/var/log/mail/info.log", "/var/log/mail/errors.log", "/var/log/httpd/*_log", "/var/log/ncftpd/misclog.txt", "/var/account/pacct", "/var/log/snort", "/var/log/bandwidth", "/var/log/explanations", "/var/log/syslog", "/var/log/user.log", "/var/log/daemons/info.log", "/var/log/daemons/warnings.log", "/var/log/daemons/errors.log", "/etc/httpd/logs/error_log", "/etc/httpd/logs/*_log", "/var/log/mysqld/mysqld.log", "/root/.ksh_history", "/root/.bash_history", "/root/.sh_history", "/root/.history", "/root/*_history", "/root/.login", "/root/.logout", "/root/.bash_logut", "/root/.Xauthority"]

class Log_Cleaner():

	def Clear():
		os.system("clear")

	def Main():
		print(Secondary_Colour+"["+Main_Colour+"Log Cleaner"+Secondary_Colour+"] Starting Log Cleaner!")
		for _ in Log_Locations:
			if Verbose == True:
				print(Secondary_Colour+"["+Main_Colour+"Log Cleaner"+Secondary_Colour+"] Trying To Remove: "+ str(_))
			if os.path.isfile(_):
				print(Secondary_Colour+"["+Main_Colour+"Log Cleaner"+Secondary_Colour+"] Removing"+Main_Colour+": "+Secondary_Colour+ str(_))
				os.remove(_)

if len(sys.argv) > 1 and os.geteuid() == 0:
	if sys.argv[1].lower() == "verbose" :
		Verbose = True
		print(Secondary_Colour+"["+Main_Colour+"Log Cleaner"+Secondary_Colour+"] Running In Verbose Mode!")
		time.sleep(2)
		Log_Cleaner.Main()
elif os.geteuid() == 0:
	Log_Cleaner.Main()
else:
	print(Secondary_Colour+"["+Main_Colour+"Log Cleaner"+Secondary_Colour+"] Please Run This Script As Root!")
