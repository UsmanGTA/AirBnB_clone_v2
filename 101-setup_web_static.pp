# Replicates task 0 in Puppet
wget { 'YEET':
	provider  => shell,
	command   => 'wget https://raw.githubusercontent.com/UsmanGTA/AirBnB_clone_v2/master/0-setup_web_static.sh && chmod u+x 0-setup_web_static.sh && sudo ./0-setup_web_static.sh'
}
