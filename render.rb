# frozen_string_literal: true

require 'toml-rb'
require 'erb'


class Config
    attr_reader :data

    def initialize(sourcefile)
        @data = TomlRB.load_file(sourcefile)
    end

    def b
        binding
    end
end

config = Config.new('project.toml')

template = File.read('templates/SWPPP_template.erb')
render = ERB.new(template)
html = render.result config.b

File.open('templates/check.html', 'w') { |f| f.write(html) }

puts 'done'
