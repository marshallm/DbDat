class check_configuration_xp_cmdshell():
	"""
	Determine current database version
	"""
	# References:
	# http://sqltidbits.com/scripts/check-if-xpcmdshell-enabled-across-multiple-servers

	TITLE    = 'Xp Cmdshell Enabled'
	CATEGORY = 'Configuration'
	TYPE     = 'sql'
	SQL    	 = "SELECT name, CAST(value as int) as value_configured, CAST(value_in_use as int) as value_in_use FROM  master.sys.configurations WHERE  name = 'xp_cmdshell'"
	
	verbose = False
	skip	= False
	result  = {}
	
	def do_check(self, *rows):
		output         = ''
		
		for row in rows:
			if 0 == row[0][1]:
				self.result['level'] = 'GREEN'
				output = 'xp_cmdshell not enabled.'
			else:
				self.result['level'] = 'RED'
				output = 'xp_cmdshell is enabled.'
		
		self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
