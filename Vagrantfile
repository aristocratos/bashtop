Vagrant.configure("2") do |config|
#  config.vm.define "centos" do |centos|
#      centos.vm.box = "centos/7"
#      centos.vm.network "private_network", ip:"192.168.77.10"
#      centos.vm.hostname = "centos"
#  end
#  config.vm.define "fedora" do |fedora|
#      fedora.vm.box = "bento/fedora-31"
#      fedora.vm.network "private_network", ip:"192.168.77.11"
#      fedora.vm.hostname = "fedora"
#  end
  config.vm.define "ubuntu" do |ubuntu|
      ubuntu.vm.box = "ubuntu/trusty64"
      ubuntu.vm.network "private_network", ip:"192.168.77.12"
      ubuntu.vm.hostname = "ubuntu"
  end
  config.vm.provision "file", source: "../bashtop", destination: "/home/vagrant/"
end