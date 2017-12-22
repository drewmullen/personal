# Create Ansible user on a RedHat machine

# Create ansible user, change the password, and give it sudo access
useradd ansible -m
echo ansible:ansible | sudo chpasswd
usermod -aG wheel ansible

#Enable password authentication
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sed -i 's/# %wheel/%wheel/g' /etc/sudoers
sudo service sshd stop
sudo service sshd start
