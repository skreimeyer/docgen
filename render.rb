# frozen_string_literal: true

require 'toml-rb'
require 'erb'

config = TomlRB.load_file('project.toml')

template = File.read('templates/SWPPP_template.erb')
render = ERB.new(template)
html = render.result_with_hash(config)

File.open('templates/check.html', 'w') { |f| f.write(html) }

puts 'done'
